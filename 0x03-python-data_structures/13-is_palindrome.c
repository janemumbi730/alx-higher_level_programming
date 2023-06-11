#include "lists.h"

/**
 * turn - reverses snd half of list
 * @head: head of snd half
 * Return: void
 */
void turn(listint_t **head)
{
	listint_t *prev;
	listint_t *curr;
	listint_t *nextt;

	prev = NULL;
	curr = *head;

	while (curr != NULL)
	{
		nextt = curr->next;
		curr->next = prev;
		prev = curr;
		curr = nextt;
	}

	*head = prev;
}

/**
 * look - compares each int of the list
 * @h1: head of first half
 * @h2: head of second half
 * Return: 1 or 0 if not equal
 */
int look(listint_t *h1, listint_t *h2)
{
	listint_t *temp1;
	listint_t *temp2;

	temp1 = h1;
	temp2 = h2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if list is a palindrome
 * @head: pointer to head list
 * Return: 0 or 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scanhalf, *middle;
	int ispal;

	slow = fast = prev_slow = *head;
	middle = NULL;
	ispal = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scanhalf = slow;
		prev_slow->next = NULL;
		turn(&scanhalf);
		ispal = look(*head, scanhalf);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scanhalf;
		}
		else
		{
			prev_slow->next = scanhalf;
		}
	}

	return (ispal);
}
